import { redirect } from "next/navigation";


const HomePage = (): JSX.Element => {
  redirect("/chat");
};

export default HomePage;
